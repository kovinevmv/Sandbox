labirint: struct.h labirint.o rwBitmap.o
	gcc labirint.o -o run_me.out rwBitmap.o
	rm *.o
labirint.o: labirint.c struct.h 
	gcc -c labirint.c
rwBitmap.o: rwBitmap.c rwBitmap.h struct.h
	gcc -c rwBitmap.c
