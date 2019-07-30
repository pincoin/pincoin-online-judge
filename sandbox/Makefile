all: sandbox

sandbox: setup.py sandbox.pyx clib/libsandbox.a
	python3 setup.py build_ext --inplace

clib/libsandbox.a:
	make -C clib libsandbox.a

clean:
	make -C clib clean
	rm -rf build *.c *.so *.log
