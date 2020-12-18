# Copyright (c) Microsoft Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Python package `playwright` is a Python library to automate Chromium,
Firefox and WebKit with a single API. Playwright is built to enable cross-browser
web automation that is ever-green, capable, reliable and fast.
"""

import playwright._api_structures
import playwright._api_types
import playwright.sync_api._generated
from playwright.sync_api._context_manager import PlaywrightContextManager

Accessibility = playwright.sync_api._generated.Accessibility
BindingCall = playwright.sync_api._generated.BindingCall
Browser = playwright.sync_api._generated.Browser
BrowserContext = playwright.sync_api._generated.BrowserContext
BrowserType = playwright.sync_api._generated.BrowserType
CDPSession = playwright.sync_api._generated.CDPSession
ChromiumBrowserContext = playwright.sync_api._generated.ChromiumBrowserContext
ConsoleMessage = playwright.sync_api._generated.ConsoleMessage
Dialog = playwright.sync_api._generated.Dialog
Download = playwright.sync_api._generated.Download
ElementHandle = playwright.sync_api._generated.ElementHandle
FileChooser = playwright.sync_api._generated.FileChooser
Frame = playwright.sync_api._generated.Frame
JSHandle = playwright.sync_api._generated.JSHandle
Keyboard = playwright.sync_api._generated.Keyboard
Mouse = playwright.sync_api._generated.Mouse
Page = playwright.sync_api._generated.Page
Playwright = playwright.sync_api._generated.Playwright
Request = playwright.sync_api._generated.Request
Response = playwright.sync_api._generated.Response
Route = playwright.sync_api._generated.Route
Selectors = playwright.sync_api._generated.Selectors
Touchscreen = playwright.sync_api._generated.Touchscreen
Video = playwright.sync_api._generated.Video
WebSocket = playwright.sync_api._generated.WebSocket
Worker = playwright.sync_api._generated.Worker

Cookie = playwright._api_structures.Cookie
ResourceTiming = playwright._api_structures.ResourceTiming
StorageState = playwright._api_structures.StorageState

DeviceDescriptor = playwright._api_types.DeviceDescriptor
Error = playwright._api_types.Error
FilePayload = playwright._api_types.FilePayload
FloatRect = playwright._api_types.FloatRect
Geolocation = playwright._api_types.Geolocation
PdfMargins = playwright._api_types.PdfMargins
ProxySettings = playwright._api_types.ProxySettings
SourceLocation = playwright._api_types.SourceLocation
TimeoutError = playwright._api_types.TimeoutError


def sync_playwright() -> PlaywrightContextManager:
    return PlaywrightContextManager()


__all__ = [
    "Accessibility",
    "BindingCall",
    "Browser",
    "BrowserContext",
    "BrowserType",
    "CDPSession",
    "ChromiumBrowserContext",
    "ConsoleMessage",
    "Cookie",
    "DeviceDescriptor",
    "Dialog",
    "Download",
    "ElementHandle",
    "Error",
    "FileChooser",
    "FilePayload",
    "FloatRect",
    "Frame",
    "Geolocation",
    "JSHandle",
    "Keyboard",
    "Mouse",
    "Page",
    "PdfMargins",
    "Playwright",
    "ProxySettings",
    "Request",
    "ResourceTiming",
    "Response",
    "Route",
    "Selectors",
    "SourceLocation",
    "StorageState",
    "sync_playwright",
    "TimeoutError",
    "Touchscreen",
    "Video",
    "WebSocket",
    "Worker",
]
