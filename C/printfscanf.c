#include <stdio.h>
int main(void) {
    printf("Hello, world!\n");
    // int age = 12;
    // printf("Age is %d\n", age);
    // age = 13;
    // printf("Age is %d\n", age);

    // // 실수형 변수에 대한 에제
    // float f = 3.14f;
    // printf("f is %f\n", f);
    // printf("f is %.2f\n", f);

    // double d = 3.1415926535897;
    // printf("d is %.4lf\n", d);

    // // 상수
    // const int YEARS = 1992;
    // const int MONTHS = 12;
    // const int DAYS = 8;
    // printf("Y/M/D %d%d%d\n", YEARS, MONTHS, DAYS);

    // // 연산
    // int add = 3 + 7;
    // printf("3 + 7 is %d\n", add);

    // // printf
    // printf("%d + %d = %d\n", 3, 7, 3 + 7);

    // //scanf 키보드 입력을 받아 저장
    // int input;
    // printf("Enter an integer: ");
    // scanf("%d", &input);
    // printf("input is %d\n", input);

    // int one, two, three;
    // printf("Enter three integers: ");
    // scanf("%d %d %d", &one, &two, &three);
    // printf("one is %d\n", one);
    // printf("two is %d\n", two);
    // printf("three is %d\n", three);

    // 문자, 문자열
    char name[20];
    printf("Enter your name: ");
    scanf("%s", name);
    printf("name is %s\n", name);

    // 문자열에 대한 에러
    char name2[5];
    printf("Enter your name: ");
    scanf("%s", name2);
    printf("name is %s\n", name2);


    // 문자열에 대한 크기 표시
    char str[20];
    // scanf("%s", str, sizeof(str));
    scanf("%s", str);
    printf("str is %s\n", str);
    
    return 0;
}