#include "named_vector.h"
#include <iostream>

named_vector::named_vector() : value(), name("Unnamed") {}

named_vector::named_vector(double x, double y, double z, const std::string &name)
    : value(x, y, z), name(name) {}

my_vector named_vector::getValue() const { return value; }

std::string named_vector::getName() const { return name; }

void named_vector::setValue(const my_vector &v) { value = v; }

void named_vector::setName(const std::string &n) { name = n; }

void named_vector::print() const
{
    std::cout << "Vector " << name << ": " << value << std::endl;
}