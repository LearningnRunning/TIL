# include <stdio.h>

int main(void) {
    printf("Hello, world!\n");
    // // ++ 뿔뿔
    // int a = 10;
    // printf(" a = %d\n", a);
    // a++;
    // printf(" a = %d\n", a);

    // int b = 20;
    // printf(" b = %d\n", ++b);
    // printf(" b = %d\n", b++);
    // printf(" b = %d\n", b);

    // 반복문
    // for, while, do while
    // // for(선언; 조건; 증감) {
    // for (int i = 0; i < 10; i++) {
    //     printf("i = %d\n", i);
    // }
    // for (int i = 0; i < 10; ++i) {
    //     printf("i = %d\n", ++i);
    // }

    // // while (조건){}

    // int i = 1;
    // while (i < 10) {
    //     printf("i = %d\n", i); // i++
    //     i++;
    // }

    // // do {} while (조건);
    // int i = 0;
    // do {
    //     printf("i = %d\n", i); // i++
    //     i++;
    // } while (i < 10);

    // // 이중 반복문
    // for (int i = 0; i < 5; i++) {
    //     for (int j = 0; j < 5; j++) {
    //         printf("i = %d, j = %d\n", i, j);
    //     }
    // }

    // // 구구단
    // for (int i = 2; i < 10; i++) {
    //     printf("\n%d 단\n", i);
    //     for (int j = 1; j < 10; j++) {
    //         printf("%d * %d = %d\n", i, j, i * j);
    //     }
    // }


    // 프로젝트 피라미드 쌓기
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}