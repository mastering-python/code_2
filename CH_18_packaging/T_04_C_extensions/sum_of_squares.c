#include <Python.h>

static PyObject* sum_of_squares(PyObject *self, PyObject
        *args){
    /* Declare the variables */
    int n;
    int total = 0;

    /* Parse the arguments */
    if(!PyArg_ParseTuple(args, "i", &n)){
        return NULL;
    }

    /* The actual summing code */
    for(int i=0; i<n; i++){
        if((i * i) < n){
            total += i * i;
        }else{
            break;
        }
    }

    /* Return the number but convert it to a Python object first
     */
    return PyLong_FromLong(total);
}

static PyMethodDef methods[] = {
    /* Register the function */
    {"sum_of_squares", sum_of_squares, METH_VARARGS,
     "Sum the perfect squares below n"},
    /* Indicate the end of the list */
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "sum_of_squares", /* Module name */
    NULL, /* Module documentation */
    -1, /* Module state, -1 means global. This parameter is
           for sub-interpreters */
    methods,
};

/* Initialize the module */
PyMODINIT_FUNC PyInit_sum_of_squares(void){
    return PyModule_Create(&module);
}

