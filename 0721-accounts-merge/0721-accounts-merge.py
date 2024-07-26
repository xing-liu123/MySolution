class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = {}
        email_to_name = {}

        def find(email) -> str:
            if parents[email] != email:
                parents[email] = find(parents[email])
            
            return parents[email]

        def union(email1, email2):
            root1 = find(email1)
            root2 = find(email2)

            if root1 != root2:
                parents[root2] = root1

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                if email not in parents:
                    parents[email] = email
                union(first_email, email)
                email_to_name[email] = name

        roots = defaultdict(list)

        for email in parents:
            root = find(email)
            roots[root].append(email)

        res = []

        for root, emails in roots.items():
            name = email_to_name[root]
            res.append([name] + sorted(emails))

        return res
                
