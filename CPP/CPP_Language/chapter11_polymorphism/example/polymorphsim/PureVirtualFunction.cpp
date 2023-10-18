#include <iostream>
#include <vector>

class Shape{    // abstract base class
private:

public:
    virtual void draw() = 0;
    virtual void rotate() = 0;
    virtual ~Shape();
};

class Open_Shape : public Shape{    // Abstract class
public:
    virtual ~Open_Shape() {}
};

class Closed_Shape : public Shape{  // Abstract class
public:
    virtual ~Closed_Shape() {}
};

class Line: public Open_Shape{      // Concrete Class
public:
    virtual void draw() override{
        std::cout << "Draw Line" << std::endl;
    }
    virtual void rotate() override{
        std::cout << "Rotate a line" << std::endl;
    }
    virtual ~Line(){}
};

class Circle : public Closed_Shape{
public:
    virtual void draw() override{
        std::cout << "Draw circle" << std::endl;
    }
    virtual void rotate() override{
        std::cout << "Rotate a circle" << std::endl;
    }
    virtual ~Circle(){}
};

class Square : public Closed_Shape{
public:
    virtual void draw() override{
        std::cout << "Draw Square" << std::endl;
    }
    virtual void rotate() override{
        std::cout << "Rotate a Square" << std::endl;
    }
    virtual ~Square(){}
};

void screen_refresh(const std::vector<Shape *> &shapes){
    std::cout << "Refreshing" << std::endl;
    for(const auto p: shapes){
        p->draw();
    }
}

int main(){
    //    Shape s;          // error
    //    Shape *p = new Shape(); // error

    //        Circle c;     // not dynamic
    //        c.draw();     // not dynamic

    //    Shape *ptr = new Circle();    //okay
    //    ptr->draw();                  //okay
    //    ptr->rotate();                //okay

    // dynamic
    Shape *s1 = new Circle();
    Shape *s2 = new Line();
    Shape *s3 = new Square();
    
    std::vector<Shape *> shapes {s1,s2,s3};
    
    //    for (const auto p: shapes) 
    //        p->draw();
        
    screen_refresh(shapes);
    
    delete s1;
    delete s2;
    delete s3;
    
    return 0;
}