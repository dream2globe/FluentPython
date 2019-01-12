#include <iostream>
using namespace std;

class Parent
{
protected:
    int a;
    int b;

public:
    Parent(int p1, int p2){
        a = p1; b = p2;
    }

    void seta(int param){
        geta();
    }

    void setb(int param){
        getb();
    }

    virtual int geta(){
        std::cout << "parent" << std::endl;       
        return a;
    }

    virtual int getb(){
        std::cout << "parent" << std::endl;
        return b;
    }
};

class Child : public Parent
{
public:
    Child(int p1, int p2)
        : Parent(p1, p2) {}

   int geta() override {
        std::cout << "child" << std::endl;
        return a;
    }

   int getb() override {
        std::cout << "child" << std::endl;
        return b;
    }
};

int main()
{
    Child* test = new Child(1, 2);
    test->seta(100);

    Parent* test2 = new Child(1, 2); // Parent의 seta의 함수도 override된 경우 자식의 함수를 호출함
    test2->seta(100);

    Child test3(3, 4);
    test3.seta(100);

    Parent test4(3, 4);
    test4.seta(100);

    return 0;
}