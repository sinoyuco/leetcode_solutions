def howMany(sentence)
    # Write your code here
    allowed = ('a'..'z').to_a + ('A'..'Z').to_a + ['-']
    count = 0
    sentence.split(" ").each do |ele|
        eb = true

        ele.split("").each_with_index do |char,i|
            if(!allowed.include?(char))
                if([',','?','.','!'].include?(char) && i == ele.length-1)
                else
                    eb = false
                end
            end
        end

        count+=1 if eb

    end
    return count
end

p howMany('he is a good programmer, he won 865 competitions, but sometimes he dont. What do you think? All test-cases should pass. Done-done?')
