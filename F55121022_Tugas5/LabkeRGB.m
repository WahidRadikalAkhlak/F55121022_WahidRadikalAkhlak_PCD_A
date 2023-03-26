% Load gambar CIELAB
labImage = imread('Cielab.jpg');

% Konversi CIELAB ke XYZ
xyzImage = lab2xyz(labImage);

% Konversi XYZ ke RGB
rgbImage = xyz2rgb(xyzImage);

% Tampilkan gambar hasil konversi
imshow(rgbImage);
