#include "my_vec.h"
#include <iostream>

my_vector::my_vector() : x(0), y(0), z(0) {}
my_vector::my_vector(double x, double y, double z) : x(x), y(y), z(z) {}
double my_vector::getX() const { return x; }
double my_vector::getY() const { return y; }
double my_vector::getZ() const { return z; }
void my_vector::setX(double x) { this->x = x; }
void my_vector::setY(double y) { this->y = y; }
void my_vector::setZ(double z) { this->z = z; }
void my_vector::print_vector() const
{
    std::cout << "(" << x << ", " << y << ", " << z << ")" << std::endl;
}
my_vector my_vector::operator+(const my_vector &other) const
{
    return my_vector(x + other.x, y + other.y, z + other.z);
}
my_vector my_vector::operator-(const my_vector &other) const
{
    return my_vector(x - other.x, y - other.y, z - other.z);
}
my_vector my_vector::operator*(double scalar) const
{
    return my_vector(x * scalar, y * scalar, z * scalar);
}
double my_vector::operator*(const my_vector &other) const
{
    return (x * other.x) + (y * other.y) + (z * other.z);
}
std::ostream &operator<<(std::ostream &os, const my_vector &v)
{
    os << "(" << v.x << ", " << v.y << ", " << v.z << ")";
    return os;
}

int main()
{
    my_vector a(1, -4, 6);
    my_vector b(0, -8, 6);
    my_vector z;
    std::cout << "a + b is " << (a + b) << std::endl;
    z.setY(14);
    std::cout << "b * 8 is" << b * 8 << std::endl;
    std::cout << "but z * b is" << z * b << std::endl;
    return 0;
}