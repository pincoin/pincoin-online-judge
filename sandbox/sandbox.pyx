from libc.stdlib cimport malloc, free

cdef extern from "judge.h":
    int py_examine(int argc, char *argv[], int user_id, int problem, int time_limit, int memory_limit)

def examine(args, user_id, problem, time_limit=2, memory_limit=128):
    cdef char ** argv

    args = [bytes(x, encoding='utf-8') for x in args]

    argv = <char**> malloc(sizeof(char*) * len(args))

    if argv is NULL:
        raise MemoryError()

    try:
        for i, s in enumerate(args):
            argv[i] = s

        return py_examine(len(args), argv, user_id, problem, time_limit, memory_limit)

    finally:
        free(argv)
