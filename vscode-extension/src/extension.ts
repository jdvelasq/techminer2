import * as vscode from 'vscode';
import { TreeViewProvider } from './treeViewProvider';
import { createWebview } from './webview';


export function activate(context: vscode.ExtensionContext) {

    const disposable = vscode.commands.registerCommand('extension.openPaperAnalysis', () => {
        createWebview(context);
    });

    context.subscriptions.push(disposable);



    const treeViewProvider = new TreeViewProvider();
    vscode.window.registerTreeDataProvider('activityBarView', treeViewProvider);

    const commandWithInputDisposable = vscode.commands.registerCommand(
        'extension.commandWithInput',
        async () => {
            const input = await vscode.window.showInputBox({
                prompt: 'Enter a parameter for this command',
            });
            vscode.window.showInformationMessage(`You entered: ${input}`);
        }
    );
    context.subscriptions.push(commandWithInputDisposable);

    const commandWithoutInputDisposable = vscode.commands.registerCommand(
        'extension.commandWithoutInput',
        () => {
            vscode.window.showInformationMessage('Command without input executed!');
        }
    );
    context.subscriptions.push(commandWithoutInputDisposable);
}

export function deactivate() {}