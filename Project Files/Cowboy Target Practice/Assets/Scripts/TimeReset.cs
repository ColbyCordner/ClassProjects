using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class TimeReset : MonoBehaviour
{
    public UnityEvent noClickEvent;
    public IntData Seconds;
    void Start()
    {
        Seconds.value = 2;
    }
    
    public IEnumerator Countdown()
    {
        while (Seconds.value > 0)
        {
            yield return new WaitForSeconds(1.0f);
            Seconds.value--;
        }
        noClickEvent.Invoke();
    }

    public void StartCountdown()
    {
        StartCoroutine(Countdown());
    }
}
