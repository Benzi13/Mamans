#ifndef ALL_VECS_H
#define ALL_VECS_H
#include "named_vector.h"
#include "../2/my_vec.h"
#include <list>
#include <string>
class all_vecs
{
private:
    std::list<named_vector> vecs;

public:
    void addVec(const named_vector &vec);
    my_vector getVecByName(const std::string &name) const;
};

#endif