#!/bin/bash

# Fungsi untuk menampilkan pesan penggunaan script
usage() {
    echo "Usage: $0 source_directory backup_location"
    exit 1
}

# Mengecek apakah jumlah parameter yang diberikan kurang dari 2
if [ $# -lt 2 ]; then
    usage
fi

# Mengambil parameter input
SOURCE_DIR=$1
BACKUP_LOCATION=$2

# Mengecek apakah direktori sumber ada
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory does not exist."
    exit 1
fi

# Membuat nama file backup berdasarkan tanggal dan waktu saat ini
BACKUP_FILENAME=$(basename "$SOURCE_DIR")_$(date +"%Y%m%d_%H%M%S").tar.gz

# Membuat file backup dan mengompresinya
tar -czvf "$BACKUP_LOCATION/$BACKUP_FILENAME" -C "$SOURCE_DIR" .

# Mengecek apakah proses backup berhasil
if [ $? -eq 0 ]; then
    echo "Backup successful: $BACKUP_LOCATION/$BACKUP_FILENAME"
else
    echo "Backup failed."
    exit 1
fi
