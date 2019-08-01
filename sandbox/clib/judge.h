#ifndef __judge_h__
#define __judge_h__

#include <unistd.h>

#define PID_STATUS_PATH_MAX 2048
#define PID_STATUS_FILE_MAX 2048

#define MEMORY_LIMIT 50000
#define TIME_LIMIT 1

#define KB 1024
#define MB 1024 * 1024

extern int test_examine(int argc, char *argv[]);
extern int py_examine(int argc, char *argv[], int user_id, int problem, int time_limit, int memory_limit);

#endif
