def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        subdomain_count = collections.Counter()
        res = []
        for website in cpdomains:
            count, domain = website.split()
            subdomain = domain.split('.')
            for i in range(len(subdomain)):
                subdomain[i] = '.'.join(subdomain[i:])
            for sub in subdomain:
                subdomain_count[sub] += int(count)

        for key, val in subdomain_count.items():
            res.append(str(val) + ' ' + key)

        return res
