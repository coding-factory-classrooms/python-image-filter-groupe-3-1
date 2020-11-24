import os


def img_filter (redirectory):
    if not os.path.exists('C:/Users/admin/Documents/repository git hub/image_filter/python-image-filter-groupe-3-1/output'):
        os.mkdir('C:/Users/admin/Documents/repository git hub/image_filter/python-image-filter-groupe-3-1/output')

    input = open(redirectory, 'r')
    output =open('output.txt','w')


    output.write(input.read())

    input.close()
    output.close()

os.mkdir('C:/Users/admin/Documents/repository git hub/image_filter/python-image-filter-groupe-3-1/output')
img_filter('C:/Users/admin/Documents/repository git hub/image_filter/python-image-filter-groupe-3-1/input.txt')
