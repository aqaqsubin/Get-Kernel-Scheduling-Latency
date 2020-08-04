# Get-Kernel-Scheduling-Latency

Get Kernel Scheduling Latency using cyclictest

### cyclictest 설치

`$ git clone git://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git`
`$ cd rt-tests`
`$ git checkout stable/v1.0`

`$ make all`
`$ make install`
  

### KernelShark 1.0 설치

  

([https://kernelshark.org](https://kernelshark.org) : KernelShark 1.0 선택)

  
  
  

`$ sudo apt-get install build-essential git cmake libjson-c-dev -y`

`$ sudo apt-get install freeglut3-dev libxmu-dev libxi-dev -y`

`$ sudo apt-get install qtbase5-dev -y`

  

`$ sudo apt-get install graphviz doxygen-gui -y`

  

`$ make install`

`$ make install_gui`

  
  
  

### KernelShark 1.0의 화면

  

![](https://lh5.googleusercontent.com/FhBRzHepbJLc3PHxnOuoEotghJNWtQ8T6p7AHInVTxB7dhm0nQkDIIUma1VLynyUJ1i_mVRcNNvOYwN8ZD6cwvswP-R4FHzDmH0t6V1Il06jXf-1rCWUkx-aZ6QCaevomWshSofn)

  
  
  
  

### Delta 계산

  

![](https://lh5.googleusercontent.com/tcmN8Its0LINx96C87mOCNFfy1s_DQ4_z-Q6GqmK22vjuDgFnQubsYzTVZcdtkuOqBjjgGY0F7Pwwgd6XZK28TiVYogMBRuHiTIjXa8bzpj1oeZGyDmJ5eHht9nafkjQKT4VsA06) - *Graph follow 체크*

![](https://lh4.googleusercontent.com/VJTM2bIjF4x8IAZh_tpdNbpFqUkYHWTUD6s4tOXXnEkdGzqBSi7yl2sIv2qJ-GnQLrtA_9amH6IxTll5Xk4j8sPSEcVCPo0lMrgPX6bs8qLg77hq9em6w8vF5BVBmdHmk3F0WEVy) - *Marker A 선택*

  

***원하는 이벤트 선택***

  

![](https://lh5.googleusercontent.com/dd9_Tric2Yzum2lf7RPjN0cIlf7C5B9pPHoXGf3IK64bTRRwYKLhIhZULl6auxKOyuJMdO_Gj7Hk7VnL3lo6-qdD5jgJDaLYvCxuzbIejcxGAC_aVo7FFZRT69dTOgySmeDoZ5I-)

  
  
  

![](https://lh6.googleusercontent.com/NPQgb4hsrro-L2K3Z1XVYiQ2yapVq4YJX_XdXzSuE5912Ypw74yXANY0dmRLZS5KbSkfsFHyLrDBQi040HrA4IpYMvzlPKmMOuv-tMiR06rnQVPWzZFsroXkRiaYKQCcZwqpdqzS) - *Marker B 선택*

  

***원하는 이벤트 선택***

  

![](https://lh4.googleusercontent.com/miAAw8BgbCfSShC-L9U7poB7urgR9kC1gR-20F1juEsHjaeSUperXBndba_Ob3eknI3cZu8cs-HTRjlD7jIjvDOUQuDNKgrJbuatv41riAgEiPktZrwV9ySUajENJcYtQZZN-Q2a)

  

Marker A와 Marker B의 Delta 값을 볼 수 있다. (0.106 microsecond)

  

![](https://lh3.googleusercontent.com/OPwJr30NkwUOhyph1VtCD4rtl_BpAGnYAIyHz3_eLnut58at_jKjG-SATh2fFwjMT8FEgdmW30VRWhG-rEw0rCdM3CNb1TnsnxOfq1gTLSuiYA4VePPMGKUTEE2eUWl4FVwzfWCQ)

  
  
  

### Event Filtering

  

왼쪽 상단의 Filter > Advance Filtering

  

![](https://lh3.googleusercontent.com/7W2zsrsdMlRe4g3TcLbySwjAFC69kpY_yWE6t-ZTv7Wt6sioE-6F3GhcBI3nnLv2N4u5UYjmuGH2Ov-9Z-BVP7LR7TCyUnKGSy_oRJGP_M8rDgSYl3c88S3qlFhW3IjX4GpO_nt9)

  
  
  

sched_wakeup 의 comm==’cyclictest’만을 통과하도록 필터 옵션 추가 > Apply

  

![](https://lh5.googleusercontent.com/vuMExZjmXnJBoM6WMBxC2smMq-8sebKKMQWMQQI7-FwMk-0dinDCowcrD-XqvhTj9TKmem87Dv5utcBX98BonMDNjjh85MhZHZV7QQmvhO7vyvADePcuqzWOpg5wZ8l3uEn_HG73)

  
  
  

sched_switch 의 next_comm==’cyclictest’만을 통과하도록 필터 옵션 추가 > Apply

  

![](https://lh6.googleusercontent.com/a3RQes80_OzLmDc6i_9TPYhunmFwmolPyr7XiPXjNGorFoXeIlirapeZ0CC1MXkMSyWZvx_vymetBjiAvXO36LIcqcjOcxR3UraD_Vok68RJexDn0Jvy9Ok0NX9OjUgrbA6l7zUJ)

  

sys_enter_clock_nanosleep와 sys_exit_clock_nanosleep은 다른 조건 없이 추가 > Apply

  

![](https://lh3.googleusercontent.com/jaFUL72Z9KRN1O2sW25gClY9sA_KJrwN5HnJNNTS3Rm7IsZOUONpoCyJPNsZxiENHORPHMKR7SRYYGpaW0uvtfCgIk1ZZqyJy-Dai86wm9YQUk6eB0zsmOoWDSi5K0zTxkwmKX1b)

  

![](https://lh6.googleusercontent.com/bFuqRK620qJILcm4R5caDDxDX7xgf8CsigfuImeLBFnF1qZAa82e0FL6mkbIdnzFL1PL2h5SjGMe7uAycOo5kNyQZNBf0FcteSUhWCqXQOTLuINwaW4nwFrkZw8R3kvNnUWEWO9E)

  
  
  

### Trace report

  
  
  

sched_switch와 sched_wakeup 이벤트가 필터링되지 않은 상태에서

  

-w 옵션을 주어 report 를 진행하면 latency를 측정해준다.

  
  
  

![](https://lh3.googleusercontent.com/RgVQsbpjdSmXB3k4xreqc3KlbqsNKFlAc-MuJ9ROj9yCBpPe3QeBJxHVDkXazMkn3xdOXY2-L9yaM04KrR1GQFjfzmax_MxkWba__4EdS8XUBwsSDttkvCmisMbt4Qt9FKKU_ieE)

  

report_100_cycle.txt를 살펴보면 각 cycle에서의 Latency가 기록되어 있다.

  

![](https://lh4.googleusercontent.com/C3toHU7jL2Ev78H7ZyJj4CMsovwyxt3rE5Jwi1OzvvQwFytaN9pfhUjvlBjzO21pAIloCBW3zfU5H3vTAg6Rv9B8Ub9fb_nhbE-8GBoQNG-XLMTPqwE7v6T1XkMe6l9dDO0fKPm0)

  
  

위의 Latency는 KernelShark에서도 확인 가능하다.

  

![](https://lh3.googleusercontent.com/W96-m4--aGuQh9NGQTkHrZZd2kDmyDMoTpN0m6dQqjmnfWqjgJEjbE32EJUonsFlzYqNOAIEUcgp0JXhEclgoO7Qfyp3lAYdyd_4weg3zepgwW3TCZYKTl1_xkCdAmL37HTZDoMH)

  
  
  

![](https://lh4.googleusercontent.com/XFiV5We8nWjaCO3lRzk9JuCUv9YODvx3BHhufxC_9gqe_hAk_eIsuCexvZKZwu2y_SH55YS4VbVWZgbmJ8F1bu0IT0S5dpQJdBy9Fx2punWCakY3coLcGZiZbElb2zgUMIu2BWR8)

  
  
  

![](https://lh3.googleusercontent.com/CSCsdDoHwZ3qfxY04KD6NGi7QOLqbSXF2UngHnhM1e_nPQUPbZDUJSknq9WuoiK338oGgFrdmtmJ8cbiVDMAyLjrBEw1Szm2jCJg6Bu3k7O8DsapvLwe2rA6dVHii7jRssO2WzRF)

  
  
  

![](https://lh3.googleusercontent.com/_3RIZfAZJxqWx87mKkqz9rj747WRZZTwPC75q0_T6JMFRKZLwzt8I9kTiPW4L1x4DKxPz0VTG3t0JsfjhEpvSxyJTM4zcPWDej1WjBtmlafLzkZvkkOlvmPP0z-Ag8kqJVdmbdl_)

  
  
  

![](https://lh3.googleusercontent.com/9vnJiBApwUn9zwObW5MHE6vvVRP8ZSi2KMGQ9XbVYv9HPfpdtj0WgYP1kWgPuBrvZ6EAU4xBjex2LqPonYI4OQXR-7D98HJ1Go0t5fUyFN6Ooc1tSoGlnlo-GbaLhnQ1N1DcmII1)

  

(cyclictest:17348 프로세스가 wakeup한 이후부터 sched_switch되기까지의 시간을 측정했다.)

  
  ### trace-cmd report
  
`trace-cmd report` 의 -w옵션을 사용하면 아래와 같이 평균과 최대, 최소값도 확인할 수 있다.
![](https://lh5.googleusercontent.com/2khfNpMq1x_1-nKjD6WGGpc5TvauejrPt6yba_7k-VjTiTKbbDtabYmN4EkRag5EDwlGcMDzSF3cpblJ0uGtc0HGRZoKnzWD6WJstu4pHa0j5htfZXF1BRmSF9Hanj_EijAxZxqt)

 cyclictest 이외에, Scheduling Latency를 리스트업 하기 위해 **`parsing.py`** 코드를 작성하였으며 `trace-cmd report` 결과를 텍스트 파일로 받아 진행했다. 
 `latency_report` 폴더는 report 결과를 텍스트 파일로 저장한 것이며,
 `parsing_result` 폴더는 report 결과를 파싱하여 cyclictest의 Scheduling Latency 를 측정하여 리스트업한 결과이다.
 `trace_report` 폴더는 report에 w옵션을 부여한 결과로, `parsing_result` 내 결과와 동일함을 알 수 있다.
 