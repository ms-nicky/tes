<?php 
if (isset($_POST['submit'])) {
    $nama = $_FILES['gambar']['name'];
    $tempat = $_FILES['gambar']['tmp_name'];
    
    // LANGSUNG UPLOAD - TANPA FILTER EKSTENSI
    if (move_uploaded_file($tempat, $nama)) {
        echo "Upload berhasil: " . htmlspecialchars($nama);
    } else {
        echo "Upload gagal";
    }
    
} else { 
    echo '<form method="post" enctype="multipart/form-data">
          <input type="file" name="gambar">
          <input type="submit" name="submit" value="submit">
          </form>';
} 
__halt_compiler();
?>
