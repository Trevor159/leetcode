class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipeMap = {}
        suppliesSet = set(supplies)
        required = defaultdict(list)
        
        ans = []
        N = len(recipes)
        
                    
        for i in range(N):
            recipeMap[recipes[i]] = i
        
        
        for i in range(N):
            recipe = recipes[i]
            
            hasIngredients = True
            
            for ingredient in ingredients[i]:
                if ingredient not in suppliesSet:
                    
                    if ingredient in recipeMap:
                        required[ingredient].append(recipe)
                        
                    hasIngredients = False
                    
            if hasIngredients:
                ans.append(recipe)
                
        
        index = 0
        
        while index < len(ans):
            supply = ans[index]
            suppliesSet.add(supply)
            
            for recipe in required[supply]:
                hasIngredients = True
                for ingredient in ingredients[recipeMap[recipe]]:
                    
                    if ingredient not in suppliesSet:
                        hasIngredients = False
                        break

                if hasIngredients:
                    ans.append(recipe)
                    
            index += 1
        
                
        return ans
                