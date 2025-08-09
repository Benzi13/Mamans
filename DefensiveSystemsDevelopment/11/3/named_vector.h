#ifndef NAMED_VECTOR_H
#define NAMED_VECTOR_H

#include "../2/my_vec.h"
#include <iostream>

class named_vector
{
private:
    my_vector value;
    std::string name;

public:
    named_vector();
    named_vector(double x, double y, double z, const std::string &name);

    my_vector getValue() const;
    std::string getName() const;

    void setValue(const my_vector &v);
    void setName(const std::string &n);

    void print() const;
};

#endif
