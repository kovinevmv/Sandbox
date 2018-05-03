
typedef struct
{
	short		bfType; 
	unsigned long	bfSize;  
	unsigned short	bfReserved1; 
	unsigned short	bfReserved2;
	unsigned long	bfOffBits;

} BITMAPFILEHEADER;


typedef struct
{
	unsigned int    biSize; 
	int             biWidth;
	int             biHeight;  
	unsigned short  biPlanes; 
	unsigned short  biBitCount;
	unsigned int    biCompression;
	unsigned int    biSizeImage;
	int             biXPelsPerMeter;
	int             biYPelsPerMeter;
	unsigned int    biClrUsed; 
	unsigned int    biClrImportant;

} BITMAPINFOHEADER;


typedef struct
{
	unsigned char  rgbBlue;
	unsigned char  rgbGreen;
	unsigned char  rgbRed; 

} RGBPIXEL;

