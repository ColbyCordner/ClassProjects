using System;
using System.Collections;
using UnityEngine;
using UnityEngine.Events;

public class DestroyBehavior : MonoBehaviour
{
    public UnityEvent OnDeathEvent;

    public float seconds = 1; 
    private WaitForSeconds wfsObj;
  
    IEnumerator Start()
    {
        wfsObj = new WaitForSeconds(seconds);
        yield return wfsObj;
        OnDeath();
        Destroy(gameObject);
    }

    public void OnDeath()
    {
        OnDeathEvent.Invoke();
    }
}