#!/bin/bash

# Batch CIA 3DS Decryptor - Linux/Arch version
# Converted from Windows batch script

echo "$(date) $(date +%H:%M:%S)" > log.txt 2>&1
echo "Decrypting..."

# Clean up existing .ncch files
rm -f *.ncch

# Process .3ds files
for file in *.3ds; do
    if [ -f "$file" ]; then
        basename="${file%.*}"
        
        # Skip if already decrypted
        if [[ ! "$basename" =~ decrypted$ ]]; then
            echo "" | ./decrypt.exe "$file" >> log.txt 2>&1
            
            ARG=""
            i=0
            
            # Process .ncch files in specific order
            for ncch_file in "$basename".*.ncch; do
                if [ -f "$ncch_file" ]; then
                    ncch_basename=$(basename "$ncch_file" .ncch)
                    
                    case "$ncch_basename" in
                        "$basename.Main") i=0 ;;
                        "$basename.Manual") i=1 ;;
                        "$basename.DownloadPlay") i=2 ;;
                        "$basename.Partition4") i=3 ;;
                        "$basename.Partition5") i=4 ;;
                        "$basename.Partition6") i=5 ;;
                        "$basename.N3DSUpdateData") i=6 ;;
                        "$basename.UpdateData") i=7 ;;
                    esac
                    
                    ARG="$ARG -i \"$ncch_file:$i:$i\""
                fi
            done
            
            wine ./makerom.exe -f cci -ignoresign -target p -o "$basename-decrypted.3ds" $ARG >> log.txt 2>&1
        fi
    fi
done

# Process .cia files
for file in *.cia; do
    if [ -f "$file" ]; then
        basename="${file%.*}"
        
        # Skip if already decrypted
        if [[ ! "$basename" =~ decrypted$ ]]; then
            wine ./ctrtool.exe -tmd "$file" > content.txt
            i=0
            ARG=""
            
            # Check for game content
            if grep -q "^T.*D.*00040000" content.txt; then
                echo "" | wine ./decrypt.exe "$file" >> log.txt 2>&1
                
                for ncch_file in "$basename".*.ncch; do
                    if [ -f "$ncch_file" ]; then
                        ARG="$ARG -i \"$ncch_file:$i:$i\""
                        ((i++))
                    fi
                done
                
                eval wine ./makerom.exe -f cia -ignoresign -target p -o "\"$basename-decfirst.cia\"" $ARG >> log.txt 2>&1
            fi
            
            # Check for patches and DLC
            if grep -E "^T.*D.*0004000E|^T.*D.*0004008C" content.txt; then
                X=0
                echo "" | wine ./decrypt.exe "$file" >> log.txt 2>&1
                
                # Find highest NCCH number
                for ncch_file in "$basename".*.ncch; do
                    if [ -f "$ncch_file" ]; then
                        ncch_basename=$(basename "$ncch_file" .ncch)
                        number=${ncch_basename#$basename.}
                        if [[ "$number" =~ ^[0-9]+$ ]] && [ "$number" -gt "$X" ]; then
                            X=$number
                        fi
                    fi
                done
                
                i=0
                while read -r line; do
                    if [ "$X" -ge "$i" ]; then
                        if [ -f "$basename.$i.ncch" ]; then
                            content_id=$(echo "$line" | cut -c25-32)
                            # Convert hex to decimal
                            id_dec=$((0x$content_id))
                            ARG="$ARG -i \"$basename.$i.ncch:$i:$id_dec\""
                            ((i++))
                        else
                            ((i++))
                        fi
                    fi
                done < <(grep "Content id" content.txt)
                
                # Check for patches
                if grep -q "^T.*D.*0004000E" content.txt; then
                    wine ./makerom.exe -f cia -ignoresign -target p -o "$basename (Patch)-decrypted.cia" $ARG >> log.txt 2>&1
                fi
                
                # Check for DLC
                if grep -q "^T.*D.*0004008C" content.txt; then
                    wine ./makerom.exe -f cia -dlc -ignoresign -target p -o "$basename (DLC)-decrypted.cia" $ARG >> log.txt 2>&1
                fi
            fi
        fi
    fi
done

# Clean up content.txt
rm -f content.txt

# Convert decfirst.cia to .cci files
for file in *-decfirst.cia; do
    if [ -f "$file" ]; then
        basename="${file%.*}"
        output_name="${basename/-decfirst/-decrypted}.cci"
        wine ./makerom.exe -ciatocci "$file" -o "$output_name" >> log.txt 2>&1
    fi
done

# Clean up temporary files
rm -f *-decfirst.cia
rm -f *.ncch

clear
echo "Finished, please press any key to exit."
read -n 1 -s
exit 0