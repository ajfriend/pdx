select
    species,
    count(*)
        as num,
from
    tbl
group by
    1
