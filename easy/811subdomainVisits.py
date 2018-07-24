class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = dict()
        ret = list()
        for item in cpdomains:
            count, domain = item.split(' ')
            count = int(count)
            d[domain] = d.get(domain, 0) + count

            domain = domain.split('.')
            
            if(len(domain) == 3):
                sub1, sub2, sub3 = domain
                d['.'.join([sub2, sub3])] = d.get('.'.join([sub2, sub3]), 0) + count
            
            d[domain[len(domain) - 1]] = d.get(domain[len(domain) - 1], 0) + count
        
        for k, v in d.items():
            ret.append(str(v) + ' ' + k)
        
        return ret
