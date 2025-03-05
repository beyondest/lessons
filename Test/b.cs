using UnityEngine;
using UnityEngine.SceneManagement;

public class GameController : MonoBehaviour
{
    public static GameController instance { get; private set; }
    public static bool isPaused { get; private set; } = false;

    [SerializeField] GameObject pauseMenu;
    [SerializeField] GameObject mainMenu;
    [SerializeField] string gameSceneName ;   


    private void Awake()
    {
        if (instance == null)
        {
            instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void Start()
    {
        Cursor.lockState = CursorLockMode.None;
        mainMenu.SetActive(true);
        pauseMenu.SetActive(false);
    }

    private void Update()
    {
        
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            if (isPaused)
            {
                Resume();
            }
            else
            {
                if (SceneManager.GetSceneByName(gameSceneName).isLoaded)
                {
                    StopGame();
                }
                else
                {
                    QuitGame();
                }
            }
        }
        if (Application.isFocused == false)
        {
            if (isPaused == false && SceneManager.GetSceneByName(gameSceneName).isLoaded)
            {
                StopGame();
            }
        }
    }

    public void PlayGame()
    {
        SceneManager.LoadSceneAsync(gameSceneName);
        pauseMenu.SetActive(false);
        mainMenu.SetActive(false);
        Cursor.lockState = CursorLockMode.Confined;
    }
    public void QuitGame()
    {
        Application.Quit();
    }
    public void StopGame()
    {
        pauseMenu.SetActive(true);
        mainMenu.SetActive(false);
        Time.timeScale = 0;
        isPaused = true;
        Cursor.lockState = CursorLockMode.None;
    }
    public void Resume()
    {
        pauseMenu.SetActive(false);
        mainMenu.SetActive(false);
        Time.timeScale = 1;
        isPaused = false;
        Cursor.lockState = CursorLockMode.Confined;
    }

}