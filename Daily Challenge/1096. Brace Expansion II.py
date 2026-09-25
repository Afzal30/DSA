class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        stack = []
        union = []
        product = ['']

        for ch in expression:
            #print()
            #print()
            #print(f" ch = {ch} stack = {stack} union = {union} product = {product}")
            if ch.isalpha():
                #print("if alpah add the charater in to every element in product", [ r + ch for r in product])
                product = [ r + ch for r in product]
            elif ch == "{":
                stack.append(union)
                stack.append(product)
                #print(" if { : appen in stack ", stack)
                union = []
                product = ['']

            elif ch == "}":
                prev_product = stack.pop()
                prev_union = stack.pop()

                #print("product + union",product + union)
                #print("prev_product", prev_product)

                #print(" iin } : ", [ p + r for r in product + union for p in prev_product])
                product = [ p + r for r in product + union for p in prev_product]
                union =prev_union

            else:
                union += product
                #print("in else union+=product",union)
                product = ['']
        
        return sorted(set(union+product))
        
