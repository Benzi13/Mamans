#ifndef MY_VECTOR_H
#define MY_VECTOR_H

#include <iostream>

class my_vector
{
private:
    double x;
    double y;
    double z;

public:
    my_vector();
    my_vector(double x, double y, double z);
    double getX() const;
    double getY() const;
    double getZ() const;
    void setX(double x);
    void setY(double y);
    void setZ(double z);
    void print_vector() const;
    my_vector operator+(const my_vector &other) const;
    my_vector operator-(const my_vector &other) const;
    my_vector operator*(double scalar) const;
    double operator*(const my_vector &other) const;
    friend std::ostream &operator<<(std::ostream &os, const my_vector &v);
};

#endif // MY_VECTOR_H