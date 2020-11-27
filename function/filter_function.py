from function.template_function import templateFunctionMulti

def filterFunction(lastImage, finalFilter, finalParamFilter, output):
    if finalFilter == 'grey':
        templateFunctionMulti(lastImage, finalFilter, finalParamFilter, output)
    if finalFilter == 'blur':
        templateFunctionMulti(lastImage, finalFilter, finalParamFilter, output)
    if finalFilter == 'dilate':
        templateFunctionMulti(lastImage, finalFilter, finalParamFilter, output)
