import pip

installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)
count = 0
for k in installed_packages_list:
    count += 1
print("totol installed packages:",count)
