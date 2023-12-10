class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        sectors = queryIP.split('.') if '.' in queryIP else queryIP.split(':')
        if (len(sectors) == 4):
            for sec in sectors:
                if not(sec.isdigit() and 0<=int(sec)<=255 and not (sec[0] == '0' and len(sec) >1)):
                    return "Neither"
            return "IPv4"
        elif (len(sectors) == 8):
            for sec in sectors:
                if not(all(c.isdigit() or c.lower() in 'abcdef' for c in sec) and len(sec)<=4 and sec):
                    return "Neither"
            return "IPv6"

        return "Neither"

# there will only be mock ip4 or ip6 therefore the first line can be done without considering other characters
# for ip4 check if the numbers are numbers and within range, and check if there are leading 0 strings
# for ip6 check if the numbers are hex, can be done by checking if each character is either number or within abcdef
# for ip6 also check for section length, to be less than or equal 4, and check for empty sections
