









* pointer function
const int* p:const修饰*p，所以*p是常量
int* const p:const修饰p,所以p是常量

* smart pointer
智能指针：如果；两个指针指向同一个内存区域，如果一个指针释放内存，则另一个指针就会变成野指针。而智能指针在一个指针释放后，另一个指针就会智能的变成nullptr。
