#include <stdio.h>
#include <stdlib.h>
#include "struct.h"

void WriteToBitmapHeader(FILE* outputFile, BITMAPFILEHEADER headerBitmap)
{
	fwrite(&headerBitmap.bfType, 2, 1, outputFile);
	fwrite(&headerBitmap.bfSize, 4, 1, outputFile);
	fwrite(&headerBitmap.bfReserved1, 2, 1, outputFile);
	fwrite(&headerBitmap.bfReserved2, 2, 1, outputFile);
	fwrite(&headerBitmap.bfOffBits, 4, 1, outputFile);
}

void WriteToBitmapInfo(FILE* outputFile, BITMAPINFOHEADER infoBitmap)
{
	fwrite(&infoBitmap.biSize, 4, 1, outputFile);
	fwrite(&infoBitmap.biWidth, 4, 1, outputFile);
	fwrite(&infoBitmap.biHeight, 4, 1, outputFile);
	fwrite(&infoBitmap.biPlanes, 2, 1, outputFile);
	fwrite(&infoBitmap.biBitCount, 2, 1, outputFile);
	fwrite(&infoBitmap.biCompression, 4, 1, outputFile);
	fwrite(&infoBitmap.biSizeImage, 4, 1, outputFile);
	fwrite(&infoBitmap.biXPelsPerMeter, 4, 1, outputFile);
	fwrite(&infoBitmap.biYPelsPerMeter, 4, 1, outputFile);
	fwrite(&infoBitmap.biClrUsed, 4, 1, outputFile);
	fwrite(&infoBitmap.biClrImportant, 4, 1, outputFile);
}

void WriteToBitmapRGB(FILE* outputFile, RGBPIXEL** arrayRGB, BITMAPINFOHEADER infoBitmap)
{

	int extraBytes = 4 - ((infoBitmap.biWidth * 3) % 4);
	if (extraBytes == 4)
	{
		extraBytes = 0;
	}

	for (int i = infoBitmap.biHeight - 1; i >= 0; i--)
	{
		for (int j = 0; j < infoBitmap.biWidth; j++)
		{
			fwrite(&arrayRGB[i][j].rgbBlue, 1, 1, outputFile);
			fwrite(&arrayRGB[i][j].rgbGreen, 1, 1, outputFile);
			fwrite(&arrayRGB[i][j].rgbRed, 1, 1, outputFile);

		}
		if (extraBytes)
		{
			for (int j = 0; j < extraBytes; j++)
			{
				fwrite("0", 1, 1, outputFile);  
			}
		}
	}

}

BITMAPFILEHEADER ReadFromBitmapHeader(FILE* inputFile)
{
	BITMAPFILEHEADER headerBitmap;
	fread(&headerBitmap.bfType, 2, 1, inputFile);
	fread(&headerBitmap.bfSize, 4, 1, inputFile);
	fread(&headerBitmap.bfReserved1, 2, 1, inputFile);
	fread(&headerBitmap.bfReserved2, 2, 1, inputFile);
	fread(&headerBitmap.bfOffBits, 4, 1, inputFile);
	return headerBitmap;
}

BITMAPINFOHEADER ReadFromBitmapInfo(FILE* inputFile)
{

	BITMAPINFOHEADER infoBitmap;
	fread(&infoBitmap.biSize, 4, 1, inputFile);
	fread(&infoBitmap.biWidth, 4, 1, inputFile);
	fread(&infoBitmap.biHeight, 4, 1, inputFile);
	fread(&infoBitmap.biPlanes, 2, 1, inputFile);
	fread(&infoBitmap.biBitCount, 2, 1, inputFile);
	fread(&infoBitmap.biCompression, 4, 1, inputFile);
	fread(&infoBitmap.biSizeImage, 4, 1, inputFile);
	fread(&infoBitmap.biXPelsPerMeter, 4, 1, inputFile);
	fread(&infoBitmap.biYPelsPerMeter, 4, 1, inputFile);
	fread(&infoBitmap.biClrUsed, 4, 1, inputFile);
	fread(&infoBitmap.biClrImportant, 4, 1, inputFile);
	return infoBitmap;
}

RGBPIXEL** ReadFromBitmapRGB(FILE* inputFile, BITMAPINFOHEADER infoBitmap)
{
	RGBPIXEL** arrayRGB = (RGBPIXEL**)malloc(sizeof(RGBPIXEL*)*infoBitmap.biHeight);
	for (int i = 0; i < infoBitmap.biHeight; i++)
	{
		arrayRGB[i] = (RGBPIXEL*)malloc(sizeof(RGBPIXEL)*infoBitmap.biWidth);
	}

	
	int extraBytes = 4 - ((infoBitmap.biWidth * 3) % 4);
	if (extraBytes == 4)
	{
		extraBytes = 0;
	}

	for (int i = infoBitmap.biHeight - 1; i >= 0; i--)
	{
		for (int j = 0; j < infoBitmap.biWidth; j++)
		{
			fread(&arrayRGB[i][j].rgbBlue, 1, 1, inputFile);
			fread(&arrayRGB[i][j].rgbGreen, 1, 1, inputFile);
			fread(&arrayRGB[i][j].rgbRed, 1, 1, inputFile);
		}

		if (extraBytes)
		{
			for (int j = 0; j < extraBytes; j++)
			{
				char zeroByte;
				fread(&zeroByte, 1, 1, inputFile);
			}
		}
	}


	return arrayRGB;

}