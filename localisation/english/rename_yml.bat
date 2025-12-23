```batch
@echo off
setlocal enabledelayedexpansion

set "OLD_PART=l_simp_chinese"
set "NEW_PART=l_english"

for %%f in (*%OLD_PART%*.yml) do (
    set "filename=%%f"
    ren "%%f" "!filename:%OLD_PART%=%NEW_PART%!"
)

echo Files renamed successfully!
```