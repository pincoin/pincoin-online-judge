#ifndef __judge_h__
#define __judge_h__

#include <unistd.h>

#define KB(x)   ((size_t) (x) << 10)
#define MB(x)   ((size_t) (x) << 20)

#define PID_STATUS_PATH_MAX 2048
#define PID_STATUS_FILE_MAX 2048

#define MEMORY_LIMIT 128
#define TIME_LIMIT 3

extern int test_examine(int argc, char *argv[]);
extern int py_examine(int argc, char *argv[], int user_id, int problem, int time_limit, int memory_limit);

#endif
