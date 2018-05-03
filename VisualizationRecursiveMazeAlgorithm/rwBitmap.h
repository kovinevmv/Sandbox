
void WriteToBitmapHeader(FILE* outfile, BITMAPFILEHEADER headerBMP);

void WriteToBitmapInfo(FILE* outfile, BITMAPINFOHEADER infoBMP);

void WriteToBitmapRGB(FILE* outfile, RGBPIXEL** arrayRGB, BITMAPINFOHEADER infoBMP);

BITMAPFILEHEADER ReadFromBitmapHeader(FILE* bitmap);

BITMAPINFOHEADER ReadFromBitmapInfo(FILE* bitmap);

RGBPIXEL** ReadFromBitmapRGB(FILE* bitmap, BITMAPINFOHEADER info);
