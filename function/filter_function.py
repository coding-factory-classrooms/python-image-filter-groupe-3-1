from function.template_function import templateFunctionMulti, templateFunctionSimple
def filterFunction(filter, lastImage, userTakeDirectory, redirectory):
    if userTakeDirectory:
        if filter == 'grey':
            templateFunctionMulti(redirectory, lastImage, filter)
        if filter == 'blur':
            templateFunctionMulti(redirectory, lastImage, filter)
        if filter == 'dilate':
            templateFunctionMulti(redirectory, lastImage, filter)
    else:
        if filter == 'grey':
            templateFunctionSimple(redirectory, lastImage, filter)
        elif filter == 'blur':
            templateFunctionSimple(redirectory, lastImage, filter)
        elif filter == 'dilate':
            templateFunctionSimple(redirectory, lastImage, filter)