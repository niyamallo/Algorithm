SELECT u.USER_ID, u.NICKNAME, SUM(b.PRICE) as TOTAL_SALES
FROM USED_GOODS_BOARD b JOIN USED_GOODS_USER u
ON b.WRITER_ID = u.USER_ID
WHERE b.STATUS = "DONE"
GROUP BY u.USER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES ASC