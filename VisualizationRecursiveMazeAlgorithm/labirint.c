#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "struct.h"
#include "rwBitmap.h"

#pragma comment(linker, "/STACK:100000000000") //BestSolutionEver
long int counter = 0;
RGBPIXEL** arrayRGB;

void savebmp(BITMAPFILEHEADER header, BITMAPINFOHEADER info)
{
	char fileNameIndex[1000];
	sprintf(fileNameIndex, "%ld", counter);
	char fileName[50] = "./Images/output_";
	strcat(fileName, fileNameIndex);
	strcat(fileName, ".bmp");

	FILE* bitmap1 = fopen(fileName, "wb");
	WriteToBitmapHeader(bitmap1, header);
	WriteToBitmapInfo(bitmap1, info);
	WriteToBitmapRGB(bitmap1, arrayRGB, info);
	fclose(bitmap1);
}

void floodFillUtil(int x, int y, int m, int n, BITMAPFILEHEADER header, BITMAPINFOHEADER info)
{
	if (x < 0 || x >= m || y < 0 || y >= n)
		return;

	if (!((arrayRGB[x][y].rgbBlue == 255) &&
		  (arrayRGB[x][y].rgbGreen == 255) && 
		  (arrayRGB[x][y].rgbRed == 255)))
		return;

	//Color head
	arrayRGB[x][y].rgbRed = 255;
	arrayRGB[x][y].rgbGreen = 165;
	arrayRGB[x][y].rgbBlue = 0;
	
	counter++;
	savebmp(header, info);
	
	//Write (x,y) of head
	printf("%d - (%d,%d)\n", (int)counter, (int)x, (int)y);

	//Correct path
	arrayRGB[x][y].rgbRed = 0;
	arrayRGB[x][y].rgbGreen = 255;
	arrayRGB[x][y].rgbBlue = 0;
	

	floodFillUtil(x + 1, y, m, n, header, info);
	floodFillUtil(x - 1, y, m, n, header, info);
	floodFillUtil(x, y + 1, m, n, header, info);
	floodFillUtil(x, y - 1, m, n, header, info);

	//Color of wrong way
	arrayRGB[x][y].rgbRed = 255;
	arrayRGB[x][y].rgbGreen = 0;
	arrayRGB[x][y].rgbBlue = 0;

}

int main()
{

	FILE* lab = fopen("./Images/input.bmp", "rb");
	BITMAPFILEHEADER header;
	BITMAPINFOHEADER info;
	header = ReadFromBitmapHeader(lab);
	info = ReadFromBitmapInfo(lab);

	arrayRGB = (RGBPIXEL**)malloc(sizeof(RGBPIXEL*)*info.biHeight);
	for (int i = 0; i < info.biHeight; i++)
	{
		arrayRGB[i] = (RGBPIXEL*)malloc(sizeof(RGBPIXEL)*info.biWidth);
	}
	arrayRGB = ReadFromBitmapRGB(lab, info);
	fclose(lab);

	int x = 0, y = 1;
	printf("Enter coordinates of start:\n");
	printf("X: ");
	scanf("%d", &x);
	printf("Y: ");
	scanf("%d", &y);

	floodFillUtil(x, y, info.biHeight, info.biWidth, header, info);

	FILE* bitmap1 = fopen("./Images/output_final.bmp", "wb");
	WriteToBitmapHeader(bitmap1, header);
	WriteToBitmapInfo(bitmap1, info);
	WriteToBitmapRGB(bitmap1, arrayRGB, info);
	fclose(bitmap1);
	
	for (int i = 0; i < info.biHeight; i++)
	{
		free(arrayRGB[i]);
	}
	free(arrayRGB);
	system("pause");
	return 0;
}

