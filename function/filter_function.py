from function.template_function import templateFunctionMulti
def filterFunction(lastImage, finalFilter, finalParamFilter, redirectory, output):
    if filter == 'grey':
        templateFunctionMulti(lastImage, finalFilter, finalParamFilter, redirectory, output)
    if filter == 'blur':
        templateFunctionMulti(lastImage, finalFilter, finalParamFilter, redirectory, output)
    if filter == 'dilate':
        templateFunctionMulti(lastImage, finalFilter, finalParamFilter, redirectory, output)