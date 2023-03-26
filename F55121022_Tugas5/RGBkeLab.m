% Load gambar RGB
rgbImage = imread('gambar.jpeg');

% Konversi RGB ke XYZ
xyzImage = rgb2xyz(rgbImage);

% Konversi XYZ ke CIELAB
labImage = xyz2lab(xyzImage);

% Tampilkan gambar hasil konversi
imshow(labImage);
