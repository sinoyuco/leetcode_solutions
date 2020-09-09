def compare_version(version1, version2)
    
    
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        i = 0
        while i < [v1.length, v2.length].min
            
            if !v1[i]
                if v2[i] === '0'
                    return 0
                else
                    return -1
                end
            end
                
            if !v2[i]
                if v1[i] === '0'
                    return 0
                else
                    return 1
                end
            end
            
            if v1[i].to_i > v2[i].to_i
                return 1
            elsif v1[i].to_i < v2[i].to_i
                return -1
            else
                i+=1
            end
        end
    
        len1 = v1.sum{|el| el.to_i}
        len2 = v2.sum{|el| el.to_i}
    
        if len1>len2
            return 1
        elsif len2>len1
            return -1
        else
            return 0
        end
    
        
end