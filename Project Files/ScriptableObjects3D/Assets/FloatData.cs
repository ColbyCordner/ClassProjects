using UnityEngine;

[CreateAssetMenu]
public class FloatData : ScriptableObject
{
    public float Speed;

    public void UpdateValue(float num)
    {
        Speed += num;
    }
}