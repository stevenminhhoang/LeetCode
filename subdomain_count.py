def subdomain_count(cpdomains):
    ans = []
    subdomain_dic = {}
    for x in cpdomains:
        count, domain = x.split(' ')
        subdomain_arr = domain.split('.')
        for i in range(len(subdomain_arr)):
            subdomain_arr[i] = '.'.join(subdomain_arr[i:])
        for sub in subdomain_arr:
            if sub in subdomain_dic:
                subdomain_dic[sub] += int(count)
            else:
                subdomain_dic[sub] = int(count)

    return ["{} {}".format(key, val) for key, val in subdomain_dic.items()]

subdomain_count(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
