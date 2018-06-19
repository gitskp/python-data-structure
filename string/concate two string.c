 #include<stdio.h>
int main(){
  int i=0,j=0;
  char str1[20],str2[20];
  puts("Enter first string");
  gets(str1);
  puts("Enter second string");
  gets(str2);
  printf("Before concatenation the strings are\n");
  puts(str1);
  puts(str2);
  while(str1[i]!='\0'){
      i++;
  }
  while(str2[j]!='\0'){
      str1[i++]=str2[j++];
  }
  str1[i]='\0';
  printf("After concatenation the strings are\n");
  puts(str1);
 return 0;
}
