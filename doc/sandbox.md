# sandboxing

* https://tbrindus.ca/on-online-judging-part-1/
* https://www.slideshare.net/Baekjoon/ss-51001155

# chroot

# ptrace

# setrlimit

## Hello, world or sum (a+b)
* C: stack(132)+data(176)=308kB / 16MB
* C++: stack(132)+data(224)=356kB / 16MB
* Java: stack(132)+data(48876)=49008kB
* Python: stack(132)+data(4324)=4488kB / 32MB
* PHP: stack(132)+data(1948)=4808kB / 256MB

## CPU

* Time limit: 1, 2, 3 sec

## Memory
When memory is not enough, it fails to map segment from shared object.

```
error while loading shared libraries: libc.so.6: failed to map segment from shared object
```

* Stack = 128MB / 256MB
* Data = 64MB / 128MB / 256MB / 512MB

### example

* C/C++: t / m
* Java: 2t+1 / 2m+16
* Python: 3t+2 / 2m+32
* PHP: t / m+512

## Files
