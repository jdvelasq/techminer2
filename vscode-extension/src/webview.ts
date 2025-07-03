import * as vscode from 'vscode';

export function createWebview(context: vscode.ExtensionContext) {
    const panel = vscode.window.createWebviewPanel(
        'paperAnalysis', // Identifier
        'Paper Analysis', // Title
        vscode.ViewColumn.One, // Display location
        {
            enableScripts: true, // Allow JavaScript
        }
    );

    // HTML content for the Webview
    panel.webview.html = getWebviewContent();

    // Handle messages from the Webview
    panel.webview.onDidReceiveMessage(
        (message) => {
            switch (message.command) {
                case 'runAnalysis':
                    vscode.window.showInformationMessage(`Running analysis for: ${message.data}`);
                    // Call your backend logic here
                    break;
            }
        },
        undefined,
        context.subscriptions
    );
}

function getWebviewContent(): string {
    return `
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Paper Analysis</title>
            <style>
                body { font-family: Arial, sans-serif; padding: 20px; }
                input, button { margin: 10px 0; }
            </style>
        </head>
        <body>
            <h1>Paper Analysis</h1>
            <label for="keywords">Keywords:</label>
            <input type="text" id="keywords" placeholder="Enter keywords" />
            <br />
            <label for="authors">Authors:</label>
            <input type="text" id="authors" placeholder="Enter authors" />
            <br />
            <button id="run">Run Analysis</button>

            <script>
                const vscode = acquireVsCodeApi();
                document.getElementById('run').addEventListener('click', () => {
                    const keywords = document.getElementById('keywords').value;
                    const authors = document.getElementById('authors').value;
                    vscode.postMessage({
                        command: 'runAnalysis',
                        data: { keywords, authors }
                    });
                });
            </script>
        </body>
        </html>
    `;
}