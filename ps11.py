def find_missing_number(nums):
    start=min(nums)
    end=max(nums)
    expected_sum=sum(range(start,end+1))
    actual_sum=sum(nums)
    return expected_sum-actual_sum
nums=[8,5,7,6]
missing=find_missing_number(nums)
print(missing)

#dictionary with salaries and find percentage of the salaries
salaries={
    "sandhya":50000,
    "sandeep":60000,
    "radha":40000
}
total=sum(salaries.values())
for salary in salaries.values():
    percentage=(salary/total)*100
    print(percentage)

    
